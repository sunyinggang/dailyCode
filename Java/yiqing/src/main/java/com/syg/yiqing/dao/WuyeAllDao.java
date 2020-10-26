package com.syg.yiqing.dao;

import com.syg.yiqing.entity.BiddingGgzy;
import com.syg.yiqing.entity.WuyeAll;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;

public interface WuyeAllDao extends JpaRepository<WuyeAll, Integer> {

    @Override
    Page<WuyeAll> findAll(Pageable pageable);
}
