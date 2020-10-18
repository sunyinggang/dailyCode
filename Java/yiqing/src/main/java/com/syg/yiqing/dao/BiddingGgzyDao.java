package com.syg.yiqing.dao;

import com.syg.yiqing.entity.BiddingGgzy;
import com.syg.yiqing.entity.SignBuilding;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;

public interface BiddingGgzyDao extends JpaRepository<BiddingGgzy, Integer> {

    @Override
    Page<BiddingGgzy> findAll(Pageable pageable);
}
